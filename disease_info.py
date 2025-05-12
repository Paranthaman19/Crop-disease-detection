# disease_info.py

DISEASE_INFO = {
    'Corn_CommonRust': {
        'symptoms': [
            'Small, circular to elongated brown pustules on leaves',
            'Pustules appear on both leaf surfaces',
            'Reddish-brown to black spores',
            'Chlorotic areas around pustules',
            'Severe infection causes leaf death'
        ],
        'management': [
            'Apply fungicides (azoxystrobin, pyraclostrobin, or propiconazole)',
            'Plant resistant hybrids',
            'Implement crop rotation with non-host crops',
            'Monitor fields regularly',
            'Maintain proper plant spacing for better air circulation'
        ],
        'environmental_conditions': {
            'temperature': '60-77°F (15-25°C)',
            'humidity': '>95%',
            'rainfall': 'Frequent light rains'
        },
        'yield_impact': 'Up to 40% yield loss in susceptible hybrids',
        'prevention': [
            'Use resistant varieties',
            'Early planting',
            'Proper field spacing',
            'Regular monitoring',
            'Maintain field sanitation'
        ]
    },

    'CornGray_Leaf_Spot': {
        'symptoms': [
            'Rectangular lesions bounded by leaf veins',
            'Gray to tan colored spots',
            'Lesions begin as small pinpoints with yellow halos',
            'Lower leaves are affected first',
            'Mature lesions are distinctly rectangular'
        ],
        'management': [
            'Apply fungicides (strobilurins, triazoles)',
            'Rotate to non-host crops for 1-2 years',
            'Remove crop debris after harvest',
            'Use resistant hybrids',
            'Improve air circulation through proper spacing'
        ],
        'environmental_conditions': {
            'temperature': '70-85°F (21-29°C)',
            'humidity': '>90%',
            'rainfall': 'Extended periods of wet weather'
        },
        'yield_impact': 'Up to 50% yield loss in severe cases',
        'prevention': [
            'Crop rotation',
            'Tillage practices to reduce residue',
            'Plant resistant varieties',
            'Optimal planting dates',
            'Balanced soil fertility'
        ]
    },

    'CornNorthern_Leaf_Blight': {
        'symptoms': [
            'Long, elliptical gray-green lesions',
            'Lesions become tan-gray as they mature',
            'Cigar-shaped lesions',
            'Lower leaves affected first',
            'Dark spores form during humid conditions'
        ],
        'management': [
            'Apply fungicides at early infection stages',
            'Plant resistant hybrids with Ht genes',
            'Rotate crops for at least one year',
            'Remove infected debris',
            'Maintain balanced soil fertility'
        ],
        'environmental_conditions': {
            'temperature': '65-80°F (18-27°C)',
            'humidity': '>90%',
            'rainfall': 'Moderate to heavy'
        },
        'yield_impact': '30-50% yield loss if infection occurs before tasseling',
        'prevention': [
            'Use resistant hybrids',
            'Crop rotation',
            'Proper residue management',
            'Balanced fertilization',
            'Regular scouting'
        ]
    },

    'Potato_EarlyBlight': {
        'symptoms': [
            'Dark brown concentric rings on leaves',
            'Target-like appearance of spots',
            'Yellowing around lesions',
            'Lower leaves affected first',
            'Leaf tissue death and defoliation'
        ],
        'management': [
            'Apply fungicides (chlorothalonil, azoxystrobin)',
            'Remove infected leaves',
            'Maintain adequate plant nutrition',
            'Proper plant spacing',
            'Avoid overhead irrigation'
        ],
        'environmental_conditions': {
            'temperature': '75-85°F (24-29°C)',
            'humidity': '90%',
            'rainfall': 'Frequent rain or dew'
        },
        'yield_impact': '20-30% yield reduction',
        'prevention': [
            'Crop rotation',
            'Clean seed potatoes',
            'Proper soil fertility',
            'Adequate plant spacing',
            'Weed control'
        ]
    },

    'Potato_LateBlight': {
        'symptoms': [
            'Water-soaked black/brown lesions',
            'White fuzzy growth on leaf undersides',
            'Rapid tissue death',
            'Dark brown surface lesions on tubers',
            'Entire plant collapse in severe cases'
        ],
        'management': [
            'Apply preventive fungicides',
            'Remove infected plants immediately',
            'Destroy volunteer potatoes',
            'Monitor weather conditions',
            'Improve air circulation'
        ],
        'environmental_conditions': {
            'temperature': '60-70°F (15-21°C)',
            'humidity': '>90%',
            'rainfall': 'Cool, wet conditions'
        },
        'yield_impact': 'Up to 100% loss if uncontrolled',
        'prevention': [
            'Use certified seed potatoes',
            'Plant resistant varieties',
            'Proper hilling of potatoes',
            'Adequate field drainage',
            'Regular field monitoring'
        ]
    },

    'RiceBrown_Spot': {
        'symptoms': [
            'Oval or circular brown spots',
            'Dark brown margin around spots',
            'Spots on leaves and glumes',
            'Infected seeds show brown spots',
            'Reduced grain quality'
        ],
        'management': [
            'Apply fungicides (propiconazole, azoxystrobin)',
            'Balanced fertilization',
            'Proper water management',
            'Remove infected stubble',
            'Use clean seeds'
        ],
        'environmental_conditions': {
            'temperature': '77-82°F (25-28°C)',
            'humidity': '>80%',
            'rainfall': 'Intermittent rainfall'
        },
        'yield_impact': '20-50% yield loss',
        'prevention': [
            'Use resistant varieties',
            'Treat seeds before planting',
            'Maintain optimal spacing',
            'Proper nutrient management',
            'Field sanitation'
        ]
    },

    'RiceLeaf_Blast': {
        'symptoms': [
            'Diamond-shaped lesions',
            'Gray centers with brown margins',
            'Lesions merge in severe cases',
            'Neck rot at panicle base',
            'White or grayish panicles'
        ],
        'management': [
            'Apply fungicides (tricyclazole, propiconazole)',
            'Split nitrogen applications',
            'Maintain continuous flooding',
            'Remove weed hosts',
            'Adjust planting dates'
        ],
        'environmental_conditions': {
            'temperature': '68-82°F (20-28°C)',
            'humidity': '>95%',
            'rainfall': 'Long dew periods'
        },
        'yield_impact': 'Up to 70% yield loss',
        'prevention': [
            'Plant resistant varieties',
            'Avoid excess nitrogen',
            'Maintain water depth',
            'Proper spacing',
            'Early planting'
        ]
    },

    'Rice_Neck_Blast': {
        'symptoms': [
            'Dark brown to black lesions on neck',
            'Rotting of panicle base',
            'White or unfilled grains',
            'Panicle breakage',
            'Complete panicle death'
        ],
        'management': [
            'Apply fungicides at heading stage',
            'Balance nitrogen fertilization',
            'Maintain consistent water levels',
            'Remove infected panicles',
            'Time planting properly'
        ],
        'environmental_conditions': {
            'temperature': '72-85°F (22-29°C)',
            'humidity': '>90%',
            'rainfall': 'Frequent rains during heading'
        },
        'yield_impact': '50-90% yield loss',
        'prevention': [
            'Use resistant cultivars',
            'Proper timing of planting',
            'Avoid dense canopy',
            'Silicon application',
            'Regular monitoring'
        ]
    },

    'Sugarcane_Bacterial Blight': {
        'symptoms': [
            'Water-soaked lesions on leaves',
            'Red stripes with yellow halos',
            'Wilting of young leaves',
            'Dark red vascular bundles',
            'Leaf chlorosis and necrosis'
        ],
        'management': [
            'Hot water treatment of setts',
            'Remove infected plants',
            'Use disease-free planting material',
            'Improve field drainage',
            'Apply copper-based bactericides'
        ],
        'environmental_conditions': {
            'temperature': '77-95°F (25-35°C)',
            'humidity': '>80%',
            'rainfall': 'High rainfall periods'
        },
        'yield_impact': '15-30% yield reduction',
        'prevention': [
            'Plant resistant varieties',
            'Clean field tools',
            'Proper field drainage',
            'Crop rotation',
            'Balanced fertilization'
        ]
    },

    'SugarcaneRed Rot': {
        'symptoms': [
            'Red discoloration in stalk',
            'White patches in infected tissue',
            'External reddening of stem',
            'Drying of upper leaves',
            'Internal tissue breakdown'
        ],
        'management': [
            'Use disease-free setts',
            'Hot water treatment',
            'Remove infected crops',
            'Avoid ratooning of infected crop',
            'Apply Trichoderma treatments'
        ],
        'environmental_conditions': {
            'temperature': '77-90°F (25-32°C)',
            'humidity': '>85%',
            'rainfall': 'High moisture conditions'
        },
        'yield_impact': '29-75% yield loss',
        'prevention': [
            'Resistant varieties',
            'Proper drainage',
            'Clean cultivation',
            'Avoid crop injuries',
            'Regular monitoring'
        ]
    },

    'WheatBrown_Rust': {
        'symptoms': [
            'Orange-brown pustules on leaves',
            'Circular to oval uredia',
            'Random distribution on leaves',
            'Pustules mainly on upper leaf surface',
            'Dark teliospores late in season'
        ],
        'management': [
            'Apply fungicides (triazoles, strobilurins)',
            'Remove volunteer wheat',
            'Plant early maturing varieties',
            'Monitor regularly',
            'Maintain proper spacing'
        ],
        'environmental_conditions': {
            'temperature': '59-77°F (15-25°C)',
            'humidity': '>95%',
            'rainfall': 'Light and frequent'
        },
        'yield_impact': '40-50% yield loss',
        'prevention': [
            'Use resistant varieties',
            'Early planting',
            'Proper fertilization',
            'Field sanitation',
            'Regular scouting'
        ]
    },

    'WheatYellow_Rust': {
        'symptoms': [
            'Yellow-orange pustules in stripes',
            'Parallel lines of pustules',
            'Starts as chlorotic flecks',
            'Severe stunting in early infection',
            'Shriveled grains'
        ],
        'management': [
            'Apply fungicides early',
            'Remove volunteer wheat',
            'Plant resistant varieties',
            'Adjust planting dates',
            'Monitor weather conditions'
        ],
        'environmental_conditions': {
            'temperature': '50-65°F (10-18°C)',
            'humidity': '>95%',
            'rainfall': 'Cool, moist conditions'
        },
        'yield_impact': 'Up to 70% yield loss',
        'prevention': [
            'Use resistant cultivars',
            'Proper planting time',
            'Balanced fertilization',
            'Field monitoring',
            'Regional disease forecasting'
        ]
    }
}

ENVIRONMENTAL_THRESHOLDS = {
    'Corn_CommonRust': {
        'temperature': {'min': 60, 'max': 77, 'optimal': 70},
        'humidity': {'min': 85, 'max': 100, 'optimal': 95},
        'rainfall': {'min': 1, 'max': 4, 'optimal': 2.5}
    },
    'CornGray_Leaf_Spot': {
        'temperature': {'min': 70, 'max': 85, 'optimal': 75},
        'humidity': {'min': 85, 'max': 100, 'optimal': 90},
        'rainfall': {'min': 2, 'max': 5, 'optimal': 3}
    },
    'CornNorthern_Leaf_Blight': {
        'temperature': {'min': 65, 'max': 80, 'optimal': 75},
        'humidity': {'min': 90, 'max': 100, 'optimal': 95},
        'rainfall': {'min': 2, 'max': 6, 'optimal': 4}
    },
    'Potato_EarlyBlight': {
        'temperature': {'min': 75, 'max': 85, 'optimal': 80},
        'humidity': {'min': 85, 'max': 100, 'optimal': 90},
        'rainfall': {'min': 1, 'max': 3, 'optimal': 2}
    },
    'Potato_LateBlight': {
        'temperature': {'min': 60, 'max': 70, 'optimal': 65},
        'humidity': {'min': 90, 'max': 100, 'optimal': 95},
        'rainfall': {'min': 2, 'max': 5, 'optimal': 3.5}
    },
    'RiceBrown_Spot': {
        'temperature': {'min': 77, 'max': 82, 'optimal': 80},
        'humidity': {'min': 80, 'max': 100, 'optimal': 85},
        'rainfall': {'min': 1, 'max': 4, 'optimal': 2.5}
    },
    'RiceLeaf_Blast': {
        'temperature': {'min': 68, 'max': 82, 'optimal': 75},
        'humidity': {'min': 95, 'max': 100, 'optimal': 95},
        'rainfall': {'min': 2, 'max': 5, 'optimal': 3.5}
    },
    'Rice_Neck_Blast': {
        'temperature': {'min': 72, 'max': 85, 'optimal': 78},
        'humidity': {'min': 90, 'max': 100, 'optimal': 95},
        'rainfall': {'min': 2, 'max': 6, 'optimal': 4}
    },
    'Sugarcane_Bacterial Blight': {
        'temperature': {'min': 77, 'max': 95, 'optimal': 85},
        'humidity': {'min': 80, 'max': 100, 'optimal': 90},
        'rainfall': {'min': 3, 'max': 7, 'optimal': 5}
    },
    'SugarcaneRed Rot': {
        'temperature': {'min': 77, 'max': 90, 'optimal': 82},
        'humidity': {'min': 85, 'max': 100, 'optimal': 90},
        'rainfall': {'min': 2, 'max': 6, 'optimal': 4}
    },
    'WheatBrown_Rust': {
        'temperature': {'min': 59, 'max': 77, 'optimal': 68},
        'humidity': {'min': 95, 'max': 100, 'optimal': 95},
        'rainfall': {'min': 1, 'max': 3, 'optimal': 2}
    },
    'WheatYellow_Rust': {
        'temperature': {'min': 50, 'max': 65, 'optimal': 58},
        'humidity': {'min': 95, 'max': 100, 'optimal': 95},
        'rainfall': {'min': 2, 'max': 4, 'optimal': 3}
    }
}

# Add healthy crop conditions for reference
HEALTHY_CROP_CONDITIONS = {
    'CornHealthy': {
        'optimal_conditions': {
            'temperature': '68-86°F (20-30°C)',
            'humidity': '60-80%',
            'rainfall': '20-30 inches during growing season'
        },
        'maintenance_tips': [
            'Maintain proper nutrient levels (N-P-K)',
            'Regular irrigation',
            'Weed control',
            'Proper plant spacing',
            'Regular monitoring for early disease detection'
        ]
    },
    'PotatoHealthy': {
        'optimal_conditions': {
            'temperature': '60-70°F (15-21°C)',
            'humidity': '60-70%',
            'rainfall': '1-2 inches per week'
        },
        'maintenance_tips': [
            'Regular hilling',
            'Balanced fertilization',
            'Proper irrigation',
            'Pest monitoring',
            'Adequate soil drainage'
        ]
    },
    'RiceHealthy': {
        'optimal_conditions': {
            'temperature': '70-85°F (21-29°C)',
            'humidity': '70-85%',
            'water_depth': '4-6 inches'
        },
        'maintenance_tips': [
            'Maintain proper water levels',
            'Balanced fertilization',
            'Weed management',
            'Regular monitoring',
            'Proper spacing'
        ]
    },
    'Sugarcane_Healthy': {
        'optimal_conditions': {
            'temperature': '80-95°F (27-35°C)',
            'humidity': '70-85%',
            'rainfall': '60-75 inches annually'
        },
        'maintenance_tips': [
            'Regular irrigation',
            'Proper nutrient management',
            'Weed control',
            'Row spacing optimization',
            'Timely harvesting'
        ]
    },
    'WheatHealthy': {
        'optimal_conditions': {
            'temperature': '60-75°F (15-24°C)',
            'humidity': '60-70%',
            'rainfall': '16-24 inches during growing season'
        },
        'maintenance_tips': [
            'Proper seeding rate',
            'Balanced fertilization',
            'Weed management',
            'Regular monitoring',
            'Proper irrigation scheduling'
        ]
    }
}