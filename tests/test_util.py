import unittest
import pathlib

from artifinder._util import _provenance_search


class ArtifinderTests(unittest.TestCase):

    def setUp(self):
        test_dir = pathlib.Path(__file__).parent
        self.search_dir1 = test_dir / 'data'
        self.target_fp1 = test_dir / 'data' / 'scatter_plot.qzv'

    def test_provenance_search(self):
        target_uuids, found_uuids, unfound_uuids = \
            _provenance_search(self.search_dir1, self.target_fp1,
                               verbose=False)

        self.assertTrue('af47db9d-bfd7-4a72-a266-cfa8defff718' in target_uuids)
        self.assertEqual(len(target_uuids), 1)

        expected_found = {'7095b508-4ae3-4791-9e7d-7ca4f5a50279',
                          '76793c84-899d-4540-8352-1a0d2255500c'}
        for e in expected_found:
            self.assertTrue(e in found_uuids)
        self.assertEqual(len(found_uuids), len(expected_found))

        expected_unfound = {'d27a741c-f7e9-48af-ad8a-a479bd89ec9e',
                            '1a4485df-2031-4e98-aecf-193ee8497f80',
                            '83f7bac5-325f-4268-8754-c816ac46c97f',
                            '79a34b19-4a78-49ec-9771-b62ca20adafd'}
        for e in expected_unfound:
            self.assertTrue(e in unfound_uuids,
                            f'{e} was not present in the unfound UUIDs.')
        self.assertEqual(len(unfound_uuids), len(expected_unfound))
