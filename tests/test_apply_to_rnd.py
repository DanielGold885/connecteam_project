from business_flows.careers_flow import fill_all_rnd_positions


def test_fill_all_rnd_positions(driver, applicant_details, cv_file_path):
    fill_all_rnd_positions(driver, applicant_details, cv_file_path)
