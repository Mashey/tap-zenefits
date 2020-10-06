import json

class PayStubs:
  schema = {
    "properties": {
        {
            "object": {
                "type": ["string", "null"]
            },
            "person": {
                "url": {
                    "type": ["string", "null"]
                },
                "object": {
                    "type": ["string", "null"]
                },
                "ref_object": {
                    "type": ["string", "null"]
                }
            },
            "url": {
                "type": ["string", "null"]
            },
            "summary": {
                "gross_pay": {
                    "amount_type": {
                        "type": ["string", "null"]
                    },
                    "amount": {
                        "type": ["string", "null"]
                    },
                    "ytd_amount": {
                        "type": ["string", "null"]
                    }
                },
                "regular_earnings": {
                    "amount_type": {
                        "type": ["string", "null"]
                    },
                    "amount": {
                        "type": ["string", "null"]
                    },
                    "ytd_amount": {
                        "type": ["string", "null"]
                    }
                },
                "company_contributions": {
                    "amount_type": {
                        "type": ["string", "null"]
                    },
                    "amount": {
                        "type": ["string", "null"]
                    },
                    "ytd_amount": {
                        "type": ["string", "null"]
                    }
                },
                "person_deductions": {
                    "amount_type": {
                        "type": ["string", "null"]
                    },
                    "amount": {
                        "type": ["string", "null"]
                    },
                    "ytd_amount": {
                        "type": ["string", "null"]
                    }
                },
                "garnishments": {
                    "amount_type": {
                        "type": ["string", "null"]
                    },
                    "amount": {
                        "type": ["string", "null"]
                    },
                    "ytd_amount": {
                        "type": ["string", "null"]
                    }
                },
                "company_taxes": {
                    "amount_type": {
                        "type": ["string", "null"]
                    },
                    "amount": {
                        "type": ["string", "null"]
                    },
                    "ytd_amount": {
                        "type": ["string", "null"]
                    }
                },
                "person_taxes": {
                    "amount_type": {
                        "type": ["string", "null"]
                    },
                    "amount": {
                        "type": ["string", "null"]
                    },
                    "ytd_amount": {
                        "type": ["string", "null"]
                    }
                },
                "imputed_pay": {
                    "amount_type": {
                        "type": ["string", "null"]
                    },
                    "amount": {
                        "type": ["string", "null"]
                    },
                    "ytd_amount": {
                        "type": ["string", "null"]
                    }
                },
                "reported_tips": {
                    "amount_type": {
                        "type": ["string", "null"]
                    },
                    "amount": {
                        "type": ["string", "null"]
                    },
                    "ytd_amount": {
                        "type": ["string", "null"]
                    }
                },
                "reimbursements": {
                    "amount_type": {
                        "type": ["string", "null"]
                    },
                    "amount": {
                        "type": ["string", "null"]
                    },
                    "ytd_amount": {
                        "type": ["string", "null"]
                    }
                },
                "cash_tips": {
                    "amount_type": {
                        "type": ["string", "null"]
                    },
                    "amount": {
                        "type": ["string", "null"]
                    },
                    "ytd_amount": {
                        "type": ["string", "null"]
                    }
                },
            },
            "earnings": [
                {
                    "amount_type": {
                        "type": ["string", "null"]
                    },
                    "ytd_amount": {
                        "type": ["string", "null"]
                    },
                    "amount": {
                        "type": ["string", "null"]
                    },
                    "name": {
                        "type": ["string", "null"]
                    },
                    "labor_group_ids": {
                            "": {
                                "type": ["string", "null"]
                            }
                    }
                },
                {
                    "amount_type": {
                        "type": ["string", "null"]
                    },
                    "ytd_amount": {
                        "type": ["string", "null"]
                    },
                    "amount": {
                        "type": ["string", "null"]
                    },
                    "name": {
                        "type": ["string", "null"]
                    },
                    "labor_group_ids": {
                            "": {
                                "type": ["string", "null"]
                            }
                    }
                },
                {
                    "amount_type": {
                        "type": ["string", "null"]
                    },
                    "ytd_amount": {
                        "type": ["string", "null"]
                    },
                    "amount": {
                        "type": ["string", "null"]
                    },
                    "name": {
                        "type": ["string", "null"]
                    },
                    "labor_group_ids": {
                            "group1": {
                                "type": ["string", "null"]
                            },
                            "group2": {
                                "type": ["string", "null"]
                            }
                    }
                }
            ],
            "company_contributions": [
                {
                    "amount_type": {
                        "type": ["string", "null"]
                    },
                    "ytd_amount": {
                        "type": ["string", "null"]
                    },
                    "amount": {
                        "type": ["string", "null"]
                    },
                    "name": {
                        "type": ["string", "null"]
                    },
                    "labor_group_ids": {
                            "group1": {
                                "type": ["string", "null"]
                            },
                            "group2": {
                                "type": ["string", "null"]
                            }
                    }
                },
                {
                    "amount_type": {
                        "type": ["string", "null"]
                    },
                    "ytd_amount": {
                        "type": ["string", "null"]
                    },
                    "amount": {
                        "type": ["string", "null"]
                    },
                    "name": {
                        "type": ["string", "null"]
                    },
                    "labor_group_ids": {
                            "group1": {
                                "type": ["string", "null"]
                            },
                            "group2": {
                                "type": ["string", "null"]
                            }
                    }
                }
            ],
            "person_deductions": [
                {
                    "amount_type": {
                        "type": ["string", "null"]
                    },
                    "ytd_amount": {
                        "type": ["string", "null"]
                    },
                    "amount": {
                        "type": ["string", "null"]
                    },
                    "name": {
                        "type": ["string", "null"]
                    },
                    "labor_group_ids": {
                            "group1": {
                                "type": ["string", "null"]
                            },
                            "group2": {
                                "type": ["string", "null"]
                            }
                    }
                },
                {
                    "amount_type": {
                        "type": ["string", "null"]
                    },
                    "ytd_amount": {
                        "type": ["string", "null"]
                    },
                    "amount": {
                        "type": ["string", "null"]
                    },
                    "name": {
                        "type": ["string", "null"]
                    },
                    "labor_group_ids": {
                            "group1": {
                                "type": ["string", "null"]
                            },
                            "group2": {
                                "type": ["string", "null"]
                            }
                    }
                },
            ],
            "garnishments": [
                {
                    "amount_type": {
                        "type": ["string", "null"]
                    },
                    "category": {
                        "type": ["string", "null"]
                    },
                    "name": {
                        "type": ["string", "null"]
                    },
                    "amount": {
                        "type": ["string", "null"]
                    },
                    "ytd_amount": {
                        "type": ["string", "null"]
                    },
                    "labor_group_ids": {
                            "group1": {
                                "type": ["string", "null"]
                            },
                            "group2": {
                                "type": ["string", "null"]
                            }
                    }
                }
            ],
            "company_taxes": [
                {
                    "amount_type": {
                        "type": ["string", "null"]
                    },
                    "ytd_amount": {
                        "type": ["string", "null"]
                    },
                    "amount": {
                        "type": ["string", "null"]
                    },
                    "name": {
                        "type": ["string", "null"]
                    },
                    "labor_group_ids": {
                            "group1": {
                                "type": ["string", "null"]
                            },
                            "group2": {
                                "type": ["string", "null"]
                            }
                    }
                },
                {
                    "amount_type": {
                        "type": ["string", "null"]
                    },
                    "ytd_amount": {
                        "type": ["string", "null"]
                    },
                    "amount": {
                        "type": ["string", "null"]
                    },
                    "name": {
                        "type": ["string", "null"]
                    },
                    "labor_group_ids": {
                            "group1": {
                                "type": ["string", "null"]
                            },
                            "group2": {
                                "type": ["string", "null"]
                            }
                    }
                }
            ],
            "person_taxes": [
                {
                    "amount_type": {
                        "type": ["string", "null"]
                    },
                    "ytd_amount": {
                        "type": ["string", "null"]
                    },
                    "amount": {
                        "type": ["string", "null"]
                    },
                    "name": {
                        "type": ["string", "null"]
                    },
                    "labor_group_ids": {
                            "group1": {
                                "type": ["string", "null"]
                            },
                            "group2": {
                                "type": ["string", "null"]
                            }
                    }
                },
                {
                    "amount_type": {
                        "type": ["string", "null"]
                    },
                    "ytd_amount": {
                        "type": ["string", "null"]
                    },
                    "amount": {
                        "type": ["string", "null"]
                    },
                    "name": {
                        "type": ["string", "null"]
                    },
                    "labor_group_ids": {
                            "group1": {
                                "type": ["string", "null"]
                            },
                            "group2": {
                                "type": ["string", "null"]
                            }
                    }
                },
                {
                    "amount_type": {
                        "type": ["string", "null"]
                    },
                    "ytd_amount": {
                        "type": ["string", "null"]
                    },
                    "amount": {
                        "type": ["string", "null"]
                    },
                    "name": {
                        "type": ["string", "null"]
                    },
                    "labor_group_ids": {
                            "group1": {
                                "type": ["string", "null"]
                            },
                            "group2": {
                                "type": ["string", "null"]
                            }
                    }
                }
            ],
            "payrun": {
                "url": {
                    "type": ["string", "null"]
                },
                "object": {
                    "type": ["string", "null"]
                },
                "ref_object": {
                    "type": ["string", "null"]
                }
            },
            "id": {
                "type": ["string", "null"],
                "key": True
            }
        },
    }
  }