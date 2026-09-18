<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AURA | Luxury Real Estate Valuation</title>
    <!-- Google Fonts & Tailwind CSS -->
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,600;0,700;1,400&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['"Plus Jakarta Sans"', 'sans-serif'],
                        serif: ['"Playfair Display"', 'serif'],
                    },
                    colors: {
                        gold: {
                            400: '#F3E5AB',
                            500: '#D4AF37',
                            600: '#AA7C11',
                        },
                        dark: {
                            900: '#0B0F17',
                            800: '#131B2E',
                            700: '#1E293B',
                        }
                    }
                }
            }
        }
    </script>
    <style>
        .gold-gradient-text {
            background: linear-[#B8860B], linear-gradient(135deg, #FFE5A3 0%, #D4AF37 50%, #AA7C11 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .glass-card {
            background: rgba(19, 27, 46, 0.7);
            backdrop-filter: blur(16px);
            border: 1px solid rgba(212, 175, 55, 0.15);
        }
    </style>
</head>
<body class="bg-dark-900 text-slate-100 font-sans min-h-screen antialiased bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-dark-800 via-dark-900 to-black">

    <div class="max-w-6xl mx-auto px-4 py-12">
        <!-- Header -->
        <header class="text-center mb-12">
            <span class="text-xs uppercase tracking-[0.3em] text-gold-500 font-semibold mb-2 block">AI-Powered Valuation</span>
            <h1 class="font-serif text-4xl md:text-6xl font-bold tracking-tight text-white mb-4">
                Estates <span class="gold-gradient-text">&</span> Valuation
            </h1>
            <p class="text-slate-400 max-w-lg mx-auto text-sm md:text-base font-light">
                Calculate precision market evaluations for premium residential properties using our machine learning model.
            </p>
        </header>

        <!-- Prediction Result Card (If present) -->
        {% if prediction_text %}
        <div class="mb-10 max-w-2xl mx-auto">
            <div class="glass-card rounded-2xl p-6 text-center border-l-4 border-l-gold-500 shadow-2xl animate-fade-in">
                <span class="text-xs uppercase tracking-widest text-slate-400">Estimated Market Value</span>
                <div class="text-3xl md:text-5xl font-serif font-bold text-gold-400 mt-2 mb-1">
                    {{ prediction_text }}
                </div>
                <p class="text-xs text-slate-500">Based on 17 architectural and spatial indicators</p>
            </div>
        </div>
        {% endif %}

        <!-- Form Card -->
        <div class="glass-card rounded-3xl p-6 md:p-10 shadow-2xl relative">
            <form action="/predict" method="POST">
                
                <!-- Section 1: Property Basics -->
                <div class="mb-8">
                    <h2 class="text-lg font-serif font-semibold text-gold-400 mb-4 border-b border-slate-800 pb-2">
                        1. Primary Details
                    </h2>
                    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
                        <div>
                            <label class="block text-xs uppercase tracking-wider text-slate-400 mb-2">Bedrooms</label>
                            <input type="number" step="any" name="bedrooms" required placeholder="e.g. 4" class="w-full bg-dark-900/80 border border-slate-800 rounded-xl px-4 py-3 text-sm focus:outline-none focus:border-gold-500 transition-colors">
                        </div>
                        <div>
                            <label class="block text-xs uppercase tracking-wider text-slate-400 mb-2">Bathrooms</label>
                            <input type="number" step="any" name="bathrooms" required placeholder="e.g. 2.5" class="w-full bg-dark-900/80 border border-slate-800 rounded-xl px-4 py-3 text-sm focus:outline-none focus:border-gold-500 transition-colors">
                        </div>
                        <div>
                            <label class="block text-xs uppercase tracking-wider text-slate-400 mb-2">Floors</label>
                            <input type="number" step="any" name="floors" required placeholder="e.g. 2" class="w-full bg-dark-900/80 border border-slate-800 rounded-xl px-4 py-3 text-sm focus:outline-none focus:border-gold-500 transition-colors">
                        </div>
                        <div>
                            <label class="block text-xs uppercase tracking-wider text-slate-400 mb-2">Postal Code</label>
                            <input type="number" step="any" name="postal_code" required placeholder="e.g. 98101" class="w-full bg-dark-900/80 border border-slate-800 rounded-xl px-4 py-3 text-sm focus:outline-none focus:border-gold-500 transition-colors">
                        </div>
                    </div>
                </div>

                <!-- Section 2: Area & Dimensions -->
                <div class="mb-8">
                    <h2 class="text-lg font-serif font-semibold text-gold-400 mb-4 border-b border-slate-800 pb-2">
                        2. Area & Dimensions (sq ft)
                    </h2>
                    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
                        <div>
                            <label class="block text-xs uppercase tracking-wider text-slate-400 mb-2">Living Area</label>
                            <input type="number" step="any" name="living_area" required placeholder="e.g. 2500" class="w-full bg-dark-900/80 border border-slate-800 rounded-xl px-4 py-3 text-sm focus:outline-none focus:border-gold-500 transition-colors">
                        </div>
                        <div>
                            <label class="block text-xs uppercase tracking-wider text-slate-400 mb-2">Lot Area</label>
                            <input type="number" step="any" name="lot_area" required placeholder="e.g. 7500" class="w-full bg-dark-900/80 border border-slate-800 rounded-xl px-4 py-3 text-sm focus:outline-none focus:border-gold-500 transition-colors">
                        </div>
                        <div>
                            <label class="block text-xs uppercase tracking-wider text-slate-400 mb-2">Renovated Lot Area</label>
                            <input type="number" step="any" name="lot_area_renov" required placeholder="e.g. 7500" class="w-full bg-dark-900/80 border border-slate-800 rounded-xl px-4 py-3 text-sm focus:outline-none focus:border-gold-500 transition-colors">
                        </div>
                        <div>
                            <label class="block text-xs uppercase tracking-wider text-slate-400 mb-2">Above Ground Area</label>
                            <input type="number" step="any" name="area_excluding_basement" required placeholder="e.g. 2000" class="w-full bg-dark-900/80 border border-slate-800 rounded-xl px-4 py-3 text-sm focus:outline-none focus:border-gold-500 transition-colors">
                        </div>
                        <div>
                            <label class="block text-xs uppercase tracking-wider text-slate-400 mb-2">Basement Area</label>
                            <input type="number" step="any" name="area_basement" required placeholder="e.g. 500" class="w-full bg-dark-900/80 border border-slate-800 rounded-xl px-4 py-3 text-sm focus:outline-none focus:border-gold-500 transition-colors">
                        </div>
                    </div>
                </div>

                <!-- Section 3: Ratings & Specs -->
                <div class="mb-8">
                    <h2 class="text-lg font-serif font-semibold text-gold-400 mb-4 border-b border-slate-800 pb-2">
                        3. Quality & Surroundings
                    </h2>
                    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
                        <div>
                            <label class="block text-xs uppercase tracking-wider text-slate-400 mb-2">Waterfront (0 or 1)</label>
                            <select name="waterfront" class="w-full bg-dark-900/80 border border-slate-800 rounded-xl px-4 py-3 text-sm focus:outline-none focus:border-gold-500 transition-colors">
                                <option value="0">No (0)</option>
                                <option value="1">Yes (1)</option>
                            </select>
                        </div>
                        <div>
                            <label class="block text-xs uppercase tracking-wider text-slate-400 mb-2">Views Rating (0-4)</label>
                            <input type="number" step="any" name="views" min="0" max="4" required placeholder="0" class="w-full bg-dark-900/80 border border-slate-800 rounded-xl px-4 py-3 text-sm focus:outline-none focus:border-gold-500 transition-colors">
                        </div>
                        <div>
                            <label class="block text-xs uppercase tracking-wider text-slate-400 mb-2">Condition (1-5)</label>
                            <input type="number" step="any" name="condition" min="1" max="5" required placeholder="3" class="w-full bg-dark-900/80 border border-slate-800 rounded-xl px-4 py-3 text-sm focus:outline-none focus:border-gold-500 transition-colors">
                        </div>
                        <div>
                            <label class="block text-xs uppercase tracking-wider text-slate-400 mb-2">Grade (1-13)</label>
                            <input type="number" step="any" name="grade" min="1" max="13" required placeholder="7" class="w-full bg-dark-900/80 border border-slate-800 rounded-xl px-4 py-3 text-sm focus:outline-none focus:border-gold-500 transition-colors">
                        </div>
                        <div>
                            <label class="block text-xs uppercase tracking-wider text-slate-400 mb-2">Year Built</label>
                            <input type="number" step="any" name="built_year" required placeholder="e.g. 1998" class="w-full bg-dark-900/80 border border-slate-800 rounded-xl px-4 py-3 text-sm focus:outline-none focus:border-gold-500 transition-colors">
                        </div>
                        <div>
                            <label class="block text-xs uppercase tracking-wider text-slate-400 mb-2">Renovation Year</label>
                            <input type="number" step="any" name="renovation_year" required placeholder="0 if never" class="w-full bg-dark-900/80 border border-slate-800 rounded-xl px-4 py-3 text-sm focus:outline-none focus:border-gold-500 transition-colors">
                        </div>
                        <div>
                            <label class="block text-xs uppercase tracking-wider text-slate-400 mb-2">Schools Nearby</label>
                            <input type="number" step="any" name="schools_nearby" required placeholder="e.g. 3" class="w-full bg-dark-900/80 border border-slate-800 rounded-xl px-4 py-3 text-sm focus:outline-none focus:border-gold-500 transition-colors">
                        </div>
                        <div>
                            <label class="block text-xs uppercase tracking-wider text-slate-400 mb-2">Airport Dist. (mi)</label>
                            <input type="number" step="any" name="distance_airport" required placeholder="e.g. 15" class="w-full bg-dark-900/80 border border-slate-800 rounded-xl px-4 py-3 text-sm focus:outline-none focus:border-gold-500 transition-colors">
                        </div>
                    </div>
                </div>

                <!-- Submit Button -->
                <div class="mt-10 text-center">
                    <button type="submit" class="bg-gradient-to-r from-gold-600 via-gold-500 to-gold-600 hover:opacity-90 text-dark-900 font-bold px-10 py-4 rounded-xl shadow-lg transform transition active:scale-95 uppercase tracking-widest text-xs">
                        Generate Valuation
                    </button>
                </div>
            </form>
        </div>
    </div>
</body>
</html>
